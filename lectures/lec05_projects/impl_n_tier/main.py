#!/usr/bin/env python3
"""
BorrowBox - Tool Sharing Application
Main entry point for the application
"""

from src.infrastructure.storage.json_storage import JsonStorage
from src.services.tool_service import ToolService
from src.ui.cli.cli_controller import CLIController
from config import DEFAULT_STORAGE_FILE

def main():
    """Application entry point"""
    # Initialize infrastructure layer
    storage = JsonStorage(DEFAULT_STORAGE_FILE)
    
    # Initialize services layer
    tool_service = ToolService(storage)
    
    # Initialize UI layer
    cli_controller = CLIController(tool_service)
    
    # Run application
    cli_controller.run()

if __name__ == "__main__":
    main()