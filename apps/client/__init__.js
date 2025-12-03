const { spawn } = require("node:child_process");

const url = "http://sms:8080";
const command =
	process.platform === "win32"
		? "start"
		: process.platform === "darwin"
			? "open"
			: "xdg-open";

const browserProcess = spawn(command, [url], { shell: true });

browserProcess.on("error", (error) => {
	console.error(`Browser process error: ${error.message}`);
});
