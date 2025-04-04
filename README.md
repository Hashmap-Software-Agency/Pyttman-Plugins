
# Pyttman Plugin Repository

 Monorepo for Pyttman Plugins, supplied by the Pyttman Framework developers.
 Welcome to the Pyttman Plugin Repository! This repository aims to house various plugins that can be used with the Pyttman framework to extend its functionality.
 
 ## Table of Contents
 
 - [About Pyttman](#about-pyttman)
 - [Available Plugins](#available-plugins)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Contributing](#contributing)
 - [License](#license)
 
 ## About Pyttman
 
 Pyttman is a framework designed to facilitate the creation of flexible and powerful applications. With a central plugin architecture, Pyttman enables easy customization and integration with external services and technologies.
 
 ## Available Plugins
 
 In this repository, you will find the following plugins:
 
 - **MongoEnginePlugin**: Integrates MongoDB via MongoEngine for easy database management.
 - **OpenAIPlugin**: Integrates OpenAI services, allowing the use of GPT models and memory management.
 
 More plugins are planned for the future, so stay tuned for updates!
 
 ## Installation
 
 Install a plugin via `pip`:
 
 ```bash
 pip install pyttman-plugin-name
 ```
 
 Replace `name` with the specific plugin you wish to install, for example, `pyttman-plugin-openai`.
 
 ## Usage
 
 To use plugins, add them to your application's configuration:
 
 ```python
 PLUGINS = [
     MongoEnginePlugin(...),
     OpenAIPlugin(...),
     # Add more plugins here
 ]
 ```
 
 Each plugin has its own settings and dependencies that should be specified based on your use case.
 
 ## Contributing
 
 We welcome contributions of all kinds! If you'd like to add a new plugin or improve existing ones, feel free to create a pull request. For larger changes, please open an issue first to discuss what you would like to change.
 
 ## License
 
 This project is licensed under the MIT License. For more information, see [LICENSE](LICENSE).
 
 ---
