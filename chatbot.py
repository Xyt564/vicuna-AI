#!/usr/bin/env python3
"""
AI CLI Chatbot using llama.cpp and Vicuna-7B
"""

import os
import sys
from pathlib import Path
from llama_cpp import Llama

# Model configuration
MODEL_PATH = "YOUR_MODEL_LOCATION"
N_CTX = 2048  # Context window size
N_GPU_LAYERS = 0  # Set to 0 for CPU, increase for GPU acceleration

# Colors for better CLI experience
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_colored(text, color, **kwargs):
    """Print colored text to terminal"""
    print(f"{color}{text}{Colors.RESET}", **kwargs)

def load_model():
    """Load the Vicuna model"""
    if not os.path.exists(MODEL_PATH):
        print_colored(f"Error: Model not found at {MODEL_PATH}", Colors.RED)
        print_colored(f"Please ensure the model file is in the 'models' folder", Colors.YELLOW)
        sys.exit(1)
    
    print_colored("Loading model...", Colors.YELLOW)
    try:
        llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=N_CTX,
            n_gpu_layers=N_GPU_LAYERS,
            verbose=False
        )
        print_colored("Model loaded successfully!\n", Colors.GREEN)
        return llm
    except Exception as e:
        print_colored(f"Error loading model: {e}", Colors.RED)
        sys.exit(1)

def format_prompt(conversation_history):
    """Format conversation history into Vicuna prompt format"""
    # Vicuna uses a specific prompt format
    prompt = ""
    for message in conversation_history:
        role = message["role"]
        content = message["content"]
        if role == "user":
            prompt += f"USER: {content}\n"
        elif role == "assistant":
            prompt += f"ASSISTANT: {content}\n"
    prompt += "ASSISTANT:"
    return prompt

def generate_response(llm, conversation_history, max_tokens=512):
    """Generate a response from the model"""
    prompt = format_prompt(conversation_history)
    
    print_colored("Assistant: ", Colors.GREEN, end="")
    
    response = ""
    try:
        output = llm(
            prompt,
            max_tokens=max_tokens,
            stop=["USER:", "ASSISTANT:"],
            echo=False,
            temperature=0.7,
            top_p=0.9,
            stream=True
        )
        
        # Stream the response
        for chunk in output:
            if 'choices' in chunk and len(chunk['choices']) > 0:
                text = chunk['choices'][0].get('text', '')
                if text:
                    print(text, end='', flush=True)
                    response += text
        
        print()  # New line after response
        return response.strip()
    
    except Exception as e:
        print_colored(f"\nError generating response: {e}", Colors.RED)
        return ""

def main():
    """Main chatbot loop"""
    print_colored("=" * 60, Colors.BLUE)
    print_colored("    AI CLI Chatbot - Vicuna 7B", Colors.BOLD)
    print_colored("=" * 60, Colors.BLUE)
    print_colored("\nCommands:", Colors.YELLOW)
    print("  'exit' or 'quit' - Exit the chatbot")
    print("  'clear' - Clear conversation history")
    print("  'help' - Show this help message\n")
    print_colored("=" * 60, Colors.BLUE)
    print()
    
    # Load the model
    llm = load_model()
    
    # Conversation history
    conversation_history = []
    
    while True:
        try:
            # Get user input
            user_input = input(f"{Colors.BLUE}You: {Colors.RESET}").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['exit', 'quit']:
                print_colored("\nGoodbye!", Colors.YELLOW)
                break
            
            elif user_input.lower() == 'clear':
                conversation_history = []
                print_colored("\nConversation history cleared!\n", Colors.YELLOW)
                continue
            
            elif user_input.lower() == 'help':
                print_colored("\nCommands:", Colors.YELLOW)
                print("  'exit' or 'quit' - Exit the chatbot")
                print("  'clear' - Clear conversation history")
                print("  'help' - Show this help message\n")
                continue
            
            # Add user message to history
            conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Generate response
            response = generate_response(llm, conversation_history)
            
            if response:
                # Add assistant response to history
                conversation_history.append({
                    "role": "assistant",
                    "content": response
                })
            
            print()  # Empty line for readability
            
        except KeyboardInterrupt:
            print_colored("\n\nInterrupted. Type 'exit' to quit.\n", Colors.YELLOW)
            continue
        except Exception as e:
            print_colored(f"\nError: {e}\n", Colors.RED)
            continue

if __name__ == "__main__":
    main()
