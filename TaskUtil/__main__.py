import os
import logging
from ruamel.yaml import YAML
from notion.client import NotionClient
import telegram


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s [%(levelname)s] - %(name)s: %(message)s')
    
    yaml = YAML(typ='safe')
    configFileName = "config.yaml"

    if not os.path.exists(configFileName):
            os.mknod(configFileName)
            with open(configFileName, "w", encoding="utf-8") as f:
                defaultConfig = {"telegram": [{"token": "Token"}, {"chat_number": "123456"}],
                        "notion": [{"token_v2": "token_v2"}, {"collection_view_url": "url"}]
                        }
                yaml.dump(defaultConfig, f)


    configFile = open("config.yaml", "r")
    configYaml = yaml.load(configFile)
    logger = logging.getLogger("Main");
    logger.info(configYaml['notion'][0]['token_v2']);
    


