from typing import List
from src.domain.entities.tool import Tool

class OutputFormatter:
    """Handles output formatting and display"""
    
    @staticmethod
    def print_header(text: str, char: str = "=") -> None:
        """Print formatted header"""
        print(f"\n{char * len(text)}")
        print(text)
        print(char * len(text))
    
    @staticmethod
    def print_section(text: str) -> None:
        """Print section header"""
        print(f"\n--- {text} ---")
    
    @staticmethod
    def print_success(message: str) -> None:
        """Print success message"""
        print(f"\n✓ {message}")
    
    @staticmethod
    def print_error(message: str) -> None:
        """Print error message"""
        print(f"\n✗ Error: {message}")
    
    @staticmethod
    def print_info(message: str) -> None:
        """Print information message"""
        print(f"\nℹ {message}")
    
    @staticmethod
    def print_tool(tool: Tool) -> None:
        """Print single tool information"""
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        if tool.photo:
            print(f"Photo: {tool.photo}")
        print(f"Owner: {tool.contact_info.name}")
        if tool.contact_info.phone:
            print(f"Phone: {tool.contact_info.phone}")
        if tool.contact_info.email:
            print(f"Email: {tool.contact_info.email}")
        print(f"Listed on: {tool.date_added}")
    
    @staticmethod
    def print_tools_list(tools: List[Tool]) -> None:
        """Print list of tools"""
        if not tools:
            OutputFormatter.print_info("No tools available yet.")
            return
        
        print(f"\nFound {len(tools)} tool(s):")
        print("-" * 50)
        
        for tool in tools:
            OutputFormatter.print_tool(tool)
            print("-" * 50)
    
    @staticmethod
    def print_menu() -> None:
        """Print main menu"""
        OutputFormatter.print_header("BorrowBox - Tool Sharing")
        print("1. List a tool")
        print("2. Search/Browse tools")
        print("3. Exit")