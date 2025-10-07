from src.ui.exceptions.ui_exceptions import UserInputException

class InputHandler:
    """Handles user input collection and basic validation"""
    
    @staticmethod
    def get_string_input(prompt: str, required: bool = True) -> str:
        """Get string input from user"""
        value = input(prompt).strip()
        if required and not value:
            raise UserInputException(f"Input is required: {prompt}")
        return value
    
    @staticmethod
    def get_optional_string_input(prompt: str) -> str:
        """Get optional string input from user"""
        return input(prompt).strip()
    
    @staticmethod
    def get_menu_choice(prompt: str, valid_choices: list) -> str:
        """Get menu choice from user"""
        choice = input(prompt).strip()
        if choice not in valid_choices:
            raise UserInputException(f"Invalid choice. Please select from: {', '.join(valid_choices)}")
        return choice
    
    @staticmethod
    def collect_tool_data() -> dict:
        """Collect all tool data from user"""
        print("\n--- Add New Tool ---")
        
        try:
            data = {
                'name': InputHandler.get_string_input("Tool name: "),
                'description': InputHandler.get_string_input("Short description: "),
                'photo': InputHandler.get_optional_string_input("Photo filename (optional): "),
                'contact_name': InputHandler.get_string_input("Your name: "),
                'phone': InputHandler.get_optional_string_input("Phone number (optional): "),
                'email': InputHandler.get_optional_string_input("Email (optional): ")
            }
            
            # Basic validation for contact methods
            if not data['phone'] and not data['email']:
                raise UserInputException("At least one contact method (phone or email) is required!")
            
            return data
            
        except UserInputException:
            raise
        except Exception as e:
            raise UserInputException(f"Error collecting input: {str(e)}")
    
    @staticmethod
    def get_search_term() -> str:
        """Get search term from user"""
        return InputHandler.get_optional_string_input(
            "Enter search term (or press Enter to see all tools): "
        )