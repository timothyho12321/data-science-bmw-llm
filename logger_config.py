"""
Logging Configuration Module
Provides centralized logging setup for the entire application
"""

import logging
import os
from datetime import datetime
from typing import Optional


class LoggerSetup:
    """Centralized logging configuration"""
    
    _loggers = {}
    
    @staticmethod
    def get_logger(name: str, log_dir: str = "logs") -> logging.Logger:
        """
        Get or create a logger with consistent formatting
        
        Parameters:
        -----------
        name : str
            Name of the logger (typically __name__)
        log_dir : str
            Directory to store log files
            
        Returns:
        --------
        logging.Logger
        """
        if name in LoggerSetup._loggers:
            return LoggerSetup._loggers[name]
        
        # Create logs directory
        os.makedirs(log_dir, exist_ok=True)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers
        if logger.handlers:
            return logger
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        simple_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # File handler (detailed, DEBUG level)
        log_file = os.path.join(log_dir, f'bmw_analysis_{datetime.now().strftime("%Y%m%d")}.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        
        # Console handler (simple, INFO level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        LoggerSetup._loggers[name] = logger
        
        return logger
    
    @staticmethod
    def log_function_call(logger: logging.Logger):
        """
        Decorator to log function entry and exit
        
        Usage:
        ------
        @LoggerSetup.log_function_call(logger)
        def my_function():
            pass
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                logger.debug(f"Entering {func.__name__} with args={args}, kwargs={kwargs}")
                try:
                    result = func(*args, **kwargs)
                    logger.debug(f"Exiting {func.__name__} successfully")
                    return result
                except Exception as e:
                    logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
                    raise
            return wrapper
        return decorator
