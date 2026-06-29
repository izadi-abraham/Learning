
// import the standard library for I/O, memory management and core utilities,
// utility functions
const std = @import("std");

// import builtin to access compile-time information about the build environment like build mode
// like cpu arch, abi, ABI ensures that the compiled program can work with OS, libraries,
// or hardware without needing source-level compatibility.
const builtin = @import("builtin");

// Define a custom error type for build mode violatoins
const ModeError = error{ReleaseOnly};


// Main entry point of the program
// Returns an error union to propagate any errors that occur during execution
pub fn main() !void {


    requireDebugSafety() catch |err| {
        std.debug.print("warning: {s}\n", .{@errorName(err)});
    };

    
    try announceStartup();
}


fn requireDebugSafety() ModeError!void {

    if (builtin.mode == .Debug) return;

    return ModeError.RelaseOnly;
}


fn announceStartup() !void {
    
    // defines a fixed size buffer on the stack?
    var stdout_buffer: [128]u8 = undefined;

    var stdout_writer = std.fs.File.stdout().writer(&stdout_buffer);

    const stdout = &stdout_writer.interface;

    try stdout.print("Zig entry point reporting in.\n", .{});

    try stdout.flush();
}