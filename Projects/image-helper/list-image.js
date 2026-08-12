  import fs from 'node:fs/promises';
  import path from 'node:path';
  import sharp from 'sharp';
  import cropConfig from './crop-config.json' with { type: 'json' }; 




  async function walk(dir) {
    const entries = await fs.readdir(dir, { withFileTypes: true } );
    const results = [];
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name)
      
      if (entry.isDirectory()) {
        const nested = await walk(fullPath);
        results.push(...nested);
      } else if(entry.name.toLowerCase().endsWith('_clean.jpg')) {
        results.push(fullPath)
      }
   }
    return results;

  }



  const sourceDir = process.argv[2];

  const cleanFiles = await walk(sourceDir);
  const TARGET_BYTES = 300 * 1024;
  const QUALITY_FLOOR = 20;


  for (const cleanFile of cleanFiles) {
    const relativePath = path.relative(sourceDir, cleanFile);

    const outputPath = cleanFile.replace(/\_clean.jpg$/i, '_reduced.jpg');

    let quality = 90;
    let buffer = await sharp(cleanFile).jpeg( { quality } ).toBuffer();

    while(buffer.length > TARGET_BYTES && quality > QUALITY_FLOOR){
      quality -= 10;
      buffer = await sharp(cleanFile).jpeg( { quality } ).toBuffer();
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

    await fs.writeFile(outputPath, buffer);
    console.log(`${path.basename(cleanFile)} -> ${path.basename(outputPath)} (${(buffer.length / 1024).toFixed(1)} KB, quality ${quality})`);
  }
