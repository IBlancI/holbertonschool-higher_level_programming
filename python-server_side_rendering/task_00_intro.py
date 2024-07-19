import os

def generate_invitations(template, attendees):
    # Validate that the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Validate that attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check if the template is empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    # Check if the attendees list is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    # Iterate over each attendee to generate personalized invitations
    for index, attendee in enumerate(attendees, start=1):
        personalized_content = template
        
        # Replace placeholders in the template with attendee information
        personalized_content = personalized_content.replace("{name}", attendee.get("name", "N/A"))
        personalized_content = personalized_content.replace("{event_title}", attendee.get("event_title", "N/A"))
        personalized_content = personalized_content.replace("{event_date}", attendee.get("event_date", "N/A"))
        personalized_content = personalized_content.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Create the output filename
        output_filename = f"output_{index}.txt"

        # Check if the output file already exists to avoid overwriting
        if os.path.exists(output_filename):
            print(f"Error: {output_filename} already exists.")
            continue

        # Try to write the personalized content to the output file
        try:
            with open(output_filename, "w") as file:
                file.write(personalized_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error: Unable to write to {output_filename}.")
            print(e)
