from dotenv import load_dotenv

load_dotenv()

from elasticsearch_agent.config import Config
from elasticsearch_chainlit.log_init import logger


class ElasticSearchConfig(Config):
    logger.info("Initialized configuration")


cfg = ElasticSearchConfig()

if __name__ == "__main__":
    logger.info(cfg.elastic_server)
    logger.info(cfg.elastic_user)
