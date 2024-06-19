

# Instagram Unfollower

Automate unfollowing users on Instagram who do not follow you back.

## Overview

This Python script leverages the Instaloader library to fetch follower and followee data from Instagram. It then uses the Instagram Private API to unfollow accounts that you follow but do not follow you back. This can be useful for managing your Instagram profile and keeping your follower/following ratio balanced.

## Features

- **Login:** Securely log in to Instagram using your credentials.
- **Retrieve Data:** Fetch your followers and followees to identify non-reciprocal follows.
- **Unfollow Automation:** Automatically unfollow users who do not follow you back.
- **Error Handling:** Basic error handling to manage exceptions during the unfollow process.

## Getting Started

### Prerequisites

- `Python 3.x`
- `instaloader` library (`pip install instaloader`)
- `instagram_private_api` library (`pip install instagram_private_api`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KChanveer10/Instagram-Unfollowers.git
   cd Instagram-Unfollowers
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Instagram credentials to `credentials.py`:
   ```python
   username = 'your_instagram_username'
   password = 'your_instagram_password'
   ```

### Usage

Run the script:
```bash
python unfollow.py
```

Follow the prompts to log in to Instagram and start the unfollow process.

**Note:** Automated interaction with Instagram's API may violate their terms of service. Use responsibly and at your own risk.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.
