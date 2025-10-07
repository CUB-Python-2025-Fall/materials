from src.services.tool_service import ToolService
from src.ui.cli.input_handlers import InputHandler
from src.ui.cli.output_formatters import OutputFormatter
from src.ui.exceptions.ui_exceptions import UserInputException
from src.domain.exceptions.domain_exceptions import DomainException
from src.infrastructure.exceptions.storage_exceptions import StorageException

class CLIController:
    """Main CLI controller that orchestrates user interactions"""
    
    def __init__(self, tool_service: ToolService):
        self.tool_service = tool_service
        self.input_handler = InputHandler()
        self.output_formatter = OutputFormatter()
        self.running = True
    
    def run(self) -> None:
        """Main application loop"""
        self.output_formatter.print_info("Welcome to BorrowBox!")
        self.output_formatter.print_info("Share tools with your neighbors easily.")
        
        while self.running:
            try:
                self._show_menu_and_handle_choice()
            except KeyboardInterrupt:
                self._handle_exit()
            except Exception as e:
                self.output_formatter.print_error(f"Unexpected error: {str(e)}")
    
    def _show_menu_and_handle_choice(self) -> None:
        """Display menu and handle user choice"""
        self.output_formatter.print_menu()
        
        try:
            choice = self.input_handler.get_menu_choice(
                "\nChoose an option (1-3): ", 
                ["1", "2", "3"]
            )
            self._handle_menu_choice(choice)
        except UserInputException as e:
            self.output_formatter.print_error(str(e))
    
    def _handle_menu_choice(self, choice: str) -> None:
        """Handle specific menu choice"""
        if choice == "1":
            self._handle_add_tool()
        elif choice == "2":
            self._handle_search_tools()
        elif choice == "3":
            self._handle_exit()
    
    def _handle_add_tool(self) -> None:
        """Handle adding a new tool"""
        try:
            tool_data = self.input_handler.collect_tool_data()
            
            tool = self.tool_service.add_tool(
                name=tool_data['name'],
                description=tool_data['description'],
                contact_name=tool_data['contact_name'],
                phone=tool_data['phone'],
                email=tool_data['email'],
                photo=tool_data['photo']
            )
            
            self.output_formatter.print_success(f"Tool '{tool.name}' added successfully!")
            
        except UserInputException as e:
            self.output_formatter.print_error(str(e))
        except DomainException as e:
            self.output_formatter.print_error(f"Invalid tool data: {str(e)}")
        except StorageException as e:
            self.output_formatter.print_error(f"Storage error: {str(e)}")
        except Exception as e:
            self.output_formatter.print_error(f"Failed to add tool: {str(e)}")
    
    def _handle_search_tools(self) -> None:
        """Handle searching for tools"""
        try:
            self.output_formatter.print_section("Search Tools")
            search_term = self.input_handler.get_search_term()
            
            tools = self.tool_service.search_tools(search_term)
            self.output_formatter.print_tools_list(tools)
            
        except StorageException as e:
            self.output_formatter.print_error(f"Storage error: {str(e)}")
        except Exception as e:
            self.output_formatter.print_error(f"Search failed: {str(e)}")
    
    def _handle_exit(self) -> None:
        """Handle application exit"""
        self.output_formatter.print_info("Thanks for using BorrowBox! Goodbye!")
        self.running = False