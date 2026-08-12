import sharp from 'sharp';
import fs from 'node:fs/promises';
import path from 'node:path';
import cropConfig from './crop-config.json' with { type: 'json' };

const TARGET_BYTES = 300 * 1024;
const QUALITY_FLOOR = 20;

async function walk(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const results = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      const nested = await walk(fullPath);
      results.push(...nested);
    } else if (
      path.extname(entry.name).toLowerCase() === '.jpg' &&
      !entry.name.includes('_clean') &&
      !entry.name.includes('_reduced')
    ) {
      results.push(fullPath);
    }
  }

  return results;
}

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function makeClean(originalFile, sourceDir) {
  const cleanPath = originalFile.replace(/\.jpg$/i, '_clean.jpg');

  if (await exists(cleanPath)) {
    console.log(`skip crop: ${path.basename(cleanPath)} already exists`);
    return cleanPath;
  }

  const relPath = path.relative(sourceDir, originalFile);
  const box = cropConfig[relPath];

  let pipeline = sharp(originalFile).rotate();
  if (box) pipeline = pipeline.extract(box);

  await pipeline.jpeg({ quality: 95 }).toFile(cleanPath);
  console.log(`${relPath} -> ${path.basename(cleanPath)}${box ? ' (cropped)' : ' (copied, no crop)'}`);

  return cleanPath;
}

async function makeReduced(cleanFile) {
  const reducedPath = cleanFile.replace(/_clean\.jpg$/i, '_reduced.jpg');

  if (await exists(reducedPath)) {
    console.log(`skip reduce: ${path.basename(reducedPath)} already exists`);
    return;
  }

  let quality = 90;
  let buffer = await sharp(cleanFile).jpeg({ quality }).toBuffer();

  while (buffer.length > TARGET_BYTES && quality > QUALITY_FLOOR) {
    quality -= 10;
    buffer = await sharp(cleanFile).jpeg({ quality }).toBuffer();
  }

  if (buffer.length > TARGET_BYTES) {
    const metadata = await sharp(cleanFile).metadata();
    let scale = 0.9;

    while (buffer.length > TARGET_BYTES && scale > 0.3) {
      const width = Math.round(metadata.width * scale);
      buffer = await sharp(cleanFile)
        .resize({ width })
        .jpeg({ quality: QUALITY_FLOOR })
        .toBuffer();
      scale -= 0.1;
    }
  }

  await fs.writeFile(reducedPath, buffer);
  console.log(
    `${path.basename(cleanFile)} -> ${path.basename(reducedPath)} (${(buffer.length / 1024).toFixed(1)} KB, quality ${quality})`
  );
}

const sourceDir = process.argv[2];
if (!sourceDir) {
  console.error('Usage: node process.js <directory>');
  process.exit(1);
}

const originals = await walk(sourceDir);

for (const original of originals) {
  const cleanFile = await makeClean(original, sourceDir);
  await makeReduced(cleanFile);
}
