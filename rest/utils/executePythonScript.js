const { spawn } = require("child_process");

const executePythonScript = async (scriptName = "", arguments = []) => {
    return new Promise((resolve, reject) => {
        if(!scriptName) return reject("Script name invalid.");

        let dataToSend = [];
        let errorToSend = "";

        let hasEncounteredError = false;

        const python = spawn('python', ['scriptName', ...arguments]);

        python.stdout.on('data', (data) => {
            dataToSend.push(data.toString());
        });

        python.on('error', (err) => {
            hasEncounteredError = true;
            errorToSend = err;
        });

        python.on('close', () => {
            if(hasEncounteredError) reject(errorToSend);
            resolve(dataToSend.join(""))
        });
    });
}

module.exports = executePythonScript;