const { spawn } = require("node:child_process");
const path = require("node:path");

// php -S localhost:8000

const phpProcess = spawn("php", ["-S", "localhost:8000"], {
    stdio: "inherit",
    cwd: path.join(__dirname, "src"),
});

phpProcess.on("close", (code) => {
    console.log(`PHP process exited with code ${code}`);
});

phpProcess.on("error", (error) => {
    console.error(`PHP process error: ${error.message}`);
});
