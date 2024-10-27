# Restaurant_booking_bot

Welcome to the **Restaurant_booking_bot** project! This bot is designed to help users make, modify, and cancel restaurant bookings. It gathers essential information such as the user's name, contact details, location, time, and guest count to streamline reservations.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Lookup Tables](#lookup-tables)
- [License](#license)

---

## Features
- **Make Bookings**: Collects user details to reserve a table or party area.
- **Modify or Cancel Bookings**: Allows users to adjust or cancel their reservations.
- **Error Handling**: Requests clarification for any unclear information.
- **Personalized Experience**: Greets users by name and verifies booking details.

---

## Project Structure
- `data/nlu.yml`: Contains NLU data, including intents, entities, and examples.
- `data/stories.yml`: Defines the conversational flow with various user stories.
- `domain.yml`: Configures intents, entities, slots, responses, and actions.
- `actions/`: Contains custom actions for additional bot functionalities.
- `config.yml`: Sets up the pipeline and policies for natural language processing.
- `lookup/`: Holds lookup files for common names or other predefined values.

---

## Setup and Installation

### Prerequisites
- [Python 3.7+](https://www.python.org/downloads/)
- [Rasa](https://rasa.com/docs/rasa/installation/)

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/renafathi04/Restaurant_booking_bot.git
   cd Hotel_booking_bot

2. **Virtual Environment** (Recommended)
   ```bash
   python -m venv rasa_env
   source rasa_env/bin/activate  # On Windows: rasa_env\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Bot**
   ```bash
   rasa train
   ```

5. **Run the Bot**
   - Start action server:
     ```bash
     rasa run actions
     ```
   - In a new terminal, launch the chatbot:
     ```bash
     rasa shell
     ```

---

## Usage

1. **Starting a Conversation**: Type "Hi" or "Hello" to initiate the bot.
2. **Booking Process**:
   - **Bot**: "Hello! Welcome to our Hotel Booking service. May I know your name and contact details?"
   - **User**: "My name is Ahmed, and my contact is 5678 8765."
3. **Providing Booking Details**:
   - **User**: "I'd like to book a table at the Kannur location for 5 people at 7 PM."
4. **Modify or Cancel**:
   - **User**: "Change the booking time to 8 PM."
   - **User**: "Cancel my booking."

---

## Configuration Overview

- **Entities**: `name`, `phone_number`, `location`, `time`, `people`, etc.
- **Intents**:
  - `greet`: Start conversation.
  - `details_collecting`: Gather user information.
  - `choose_location`, `quantity_details`, `timings`: Collect booking preferences.
  - `confirm_booking`, `cancel_booking`, `modify_booking`: Booking actions.

---

## Lookup Tables

The bot references a lookup table for names and other values:
```yaml
lookup_tables:
  - name: "names"
    lookup: "data/lookups/names.txt"
```
---

## License

This project is licensed under the MIT License. See `LICENSE` for details.


