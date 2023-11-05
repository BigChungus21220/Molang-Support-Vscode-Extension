// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "molang-support" is now active!');
	vscode.window.showInformationMessage('Opened a json file');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('molang-support.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from Molang Support!');
	});

	/*
	for all json files
	on startup
		if not in a workspace, do nothing
		check for molang folders (assume parent dir is directory of target files)
	on file active
		check all strings in json files in directories that are linked to a molang folder for a molang file path
			check for file in molang folder
				mark as path and display hover note of "link to molang file"
			if not do nothing
	on json file edit string
		check if string 
	*/

	const editor = vscode.window.activeTextEditor;
	//const 

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
