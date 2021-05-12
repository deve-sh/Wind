const { spawn } = require("child_process");

const executePythonScript = async (scriptName = "", arguments = []) => {
    return new Promise((resolve, reject) => {
        if(!scriptName) return reject("Script name invalid.");
        let dataToSend;

        const python = spawn('python', ['scriptName', ...arguments]);

        python.stdout.on('data', function (data) {
            dataToSend = data.toString();
        });

        python.on('close', () => resolve(dataToSend));
    });
}

module.exports = executePythonScript;