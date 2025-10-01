import json
import os
from datetime import datetime

# File to store tool data
DATA_FILE = "tools.json"

def load_tools():
    """Load tools from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tools(tools):
    """Save tools to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(tools, f, indent=2)

def add_tool():
    """Add a new tool to the list"""
    print("\n--- Add New Tool ---")
    name = input("Tool name: ").strip()
    if not name:
        print("Tool name cannot be empty!")
        return
    
    description = input("Short description: ").strip()
    photo = input("Photo filename (optional): ").strip()
    contact_name = input("Your name: ").strip()
    phone = input("Phone number (optional): ").strip()
    email = input("Email (optional): ").strip()
    
    if not contact_name:
        print("Contact name is required!")
        return
    
    if not phone and not email:
        print("At least one contact method (phone or email) is required!")
        return
    
    # Create tool entry
    tool = {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "name": name,
        "description": description,
        "photo": photo,
        "contact_name": contact_name,
        "phone": phone,
        "email": email,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    # Load existing tools and add new one
    tools = load_tools()
    tools.append(tool)
    save_tools(tools)
    
    print(f"\nTool '{name}' added successfully!")

def search_tools():
    """Search for tools"""
    tools = load_tools()
    
    if not tools:
        print("\nNo tools available yet.")
        return
    
    print("\n--- Search Tools ---")
    search_term = input("Enter search term (or press Enter to see all tools): ").strip().lower()
    
    matching_tools = []
    for tool in tools:
        if not search_term or search_term in tool["name"].lower() or search_term in tool["description"].lower():
            matching_tools.append(tool)
    
    if not matching_tools:
        print("No tools found matching your search.")
        return
    
    print(f"\nFound {len(matching_tools)} tool(s):")
    print("-" * 50)
    
    for tool in matching_tools:
        print(f"Tool: {tool['name']}")
        print(f"Description: {tool['description']}")
        if tool['photo']:
            print(f"Photo: {tool['photo']}")
        print(f"Owner: {tool['contact_name']}")
        if tool['phone']:
            print(f"Phone: {tool['phone']}")
        if tool['email']:
            print(f"Email: {tool['email']}")
        print(f"Listed on: {tool['date_added']}")
        print("-" * 50)

def show_menu():
    """Display main menu"""
    print("\n=== BorrowBox - Tool Sharing ===")
    print("1. List a tool")
    print("2. Search/Browse tools")
    print("3. Exit")
    return input("\nChoose an option (1-3): ").strip()

def main():
    """Main program loop"""
    print("Welcome to BorrowBox!")
    print("Share tools with your neighbors easily.")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_tool()
        elif choice == "2":
            search_tools()
        elif choice == "3":
            print("\nThanks for using BorrowBox! Goodbye!")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()