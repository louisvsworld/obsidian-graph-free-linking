import os
import urllib.parse

def create_obsidian_url_link(note_title, link_text, is_raw_url=False):
    """
    Generates a URL-encoded, graph-free Markdown link for Obsidian.
    If is_raw_url is True, it uses the note_title directly as the URL.
    """
    if is_raw_url:
        obsidian_url = note_title
    else:
        vault_name = "Evolution Engine"  # Your vault name
        encoded_note_title = urllib.parse.quote(note_title)
        obsidian_url = f"obsidian://open?vault={vault_name}&file={encoded_note_title}"
    
    markdown_link = f"[{link_text}]({obsidian_url})"
    return markdown_link

def manual_input_mode(script_dir):
    """Handles the creation of single links via manual user input from note titles."""
    generated_links = []
    print("\n--- Manual Input Mode ---")
    while True:
        note = input("Enter the note title (e.g., 'My Note Title'): ")
        text = input(f"Enter the display text for the link (or press Enter to use '{note}'): ")
        
        if not text.strip():
            text = note
            
        generated_link = create_obsidian_url_link(note, text)
        
        print("\n" + "="*30)
        print("Your Obsidian Markdown link is:")
        print(generated_link)
        print("="*30)
        
        generated_links.append(generated_link)
        
        cont = input("Do you want to create another link? (Y/N): ").strip().lower()
        if cont != 'y':
            break
            
    if generated_links:
        save_links_to_file(generated_links, script_dir)

def batch_file_mode(script_dir):
    """
    Handles batch creation from a .txt file containing raw Obsidian URLs.
    The source file must be in a 'Batch Processing' sub-folder.
    """
    generated_links = []
    print("\n--- Batch File Mode (from Raw Obsidian URLs) ---")
    
    batch_folder_path = os.path.join(script_dir, "Batch Processing")
    
    if not os.path.isdir(batch_folder_path):
        print(f"\nERROR: The 'Batch Processing' folder does not exist.")
        print(f"Please create it in the same directory as the script: {script_dir}")
        return

    try:
        filename = input(f"Enter the name of your batch file (must be inside 'Batch Processing'): ").strip()
        full_path = os.path.join(batch_folder_path, filename)

        with open(full_path, 'r', encoding='utf-8') as f:
            raw_urls = [line.strip() for line in f if line.strip()]
        
        if not raw_urls:
            print("The file is empty. No links to process.")
            return

        print(f"\nFound {len(raw_urls)} URLs to process. Please provide display text for each.")
        print("-" * 40)

        for i, url in enumerate(raw_urls):
            print(f"Link {i+1}/{len(raw_urls)}: {url}")
            display_text = input("Enter the display text for this link: ")
            
            generated_link = create_obsidian_url_link(url, display_text, is_raw_url=True)
            generated_links.append(generated_link)
            print("-" * 40)
        
        print("\nBatch processing complete.")
        if generated_links:
            save_links_to_file(generated_links, script_dir)

    except FileNotFoundError:
        print(f"\nERROR: File '{filename}' not found inside the 'Batch Processing' folder.")
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")

def save_links_to_file(links, script_dir):
    """Saves a list of generated links to a file, with an overwrite check."""
    save = input("\nDo you want to save the generated links to a file? (Y/N): ").strip().lower()
    if save != 'y':
        print("\nYou chose not to save. Here are the generated links:")
        print("-" * 40)
        for link in links:
            print(link)
        print("-" * 40)
        return

    try:
        output_folder_path = os.path.join(script_dir, "Generated Links")
        os.makedirs(output_folder_path, exist_ok=True)

        while True:
            filename_input = input("Enter the destination file name for the output: ").strip()
            if not filename_input.lower().endswith('.txt'):
                filename_input += '.txt'

            full_path = os.path.join(output_folder_path, filename_input)

            if os.path.exists(full_path):
                overwrite = input(f"WARNING: '{filename_input}' already exists. Overwrite? (Y/N): ").strip().lower()
                if overwrite == 'y':
                    break  # Exit loop to proceed with saving
                else:
                    print("Save cancelled. Please enter a new filename.")
                    continue # Ask for a new filename
            else:
                break # File doesn't exist, proceed with saving

        with open(full_path, 'w', encoding='utf-8') as f:
            for link in links:
                f.write(link + '\n\n')
        
        print(f"\nSUCCESS: {len(links)} links saved to {full_path}")

    except Exception as e:
        print(f"\nERROR: Could not save the file. Reason: {e}")

def main():
    """Main function to run the link generator."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        print("\nFATAL ERROR: Could not determine the script's directory.")
        print("Please run this script from a command line by navigating to its folder first.")
        input("Press Enter to exit.")
        return

    print("--- Obsidian Graph-Free Link Generator v2.4 ---")
    print(f"Script is running from: {script_dir}")
    
    while True:
        mode = input("\nChoose mode: (1) Manual Input | (2) Batch File | (Q) Quit: ").strip().lower()
        
        if mode == '1':
            manual_input_mode(script_dir)
        elif mode == '2':
            batch_file_mode(script_dir)
        elif mode == 'q':
            print("\nExiting program.")
            break
        else:
            print("Invalid input. Please enter 1, 2, or Q.")

if __name__ == "__main__":
    main()
