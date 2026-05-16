from utils.logger import logger

logging.basicConfig(
    level=logger.info,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)