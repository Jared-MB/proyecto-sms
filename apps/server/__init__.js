const { spawn } = require("node:child_process");

const pythonProcess = spawn("../../venv/Scripts/python.exe", ["./app.py"], {
    stdio: "inherit",
    cwd: __dirname,
});

pythonProcess.on("close", (code) => {
    console.log(`Python process exited with code ${code}`);
});

pythonProcess.on("error", (error) => {
    console.error(`Python process error: ${error.message}`);
});
