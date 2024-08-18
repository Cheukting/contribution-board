# contribution-board

## Set up access token as environment variables

The following tokens can be added as environment variables to add extra functionalities:

- `TOKEN`: GitHub token to increase the GitHub API request limits, useful for developing locally, can be omit when running on GitHub action. It will be something that starts with `Bearer github` followed by a unique sequence of characters. [Check here to learn how to create a GitHub access token for personal use](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

- `MASTODON_TOKEN`: Post to your Mastodon account. If you want to post to your Mastodon account when there is a new PR/ merged PR, then you have to provide your Mastodon handle in `config.py` and set up a token for access. The token will be something that starts with `Bearer ` followed by a unique sequence of characters. Log in to your Mastodon account on the web browser and simply go to `https://<your_mastodon_domain>/settings/applications` to create a new application to obtain a Mastodon token. Make sure you have given `write` access to your application.

## Extra program needed

If you are developing locally, you will need a few extra program (not in Python) other than Python and the libraries listed at `requirements.txt` to run. They are:

- ImageMagick (Install instruction)
- Potrace (Intall instrustion)

You may want to install them before developing locally.

## Schedule running on GitHub action

Other than trigger by a `push` event, the GitHub action workflow is set to run every day at a certain time, the time is set randomly. To set your own time, you can do to the `generate_svg.yml` and chage the `cron` setting. To understand more about how to set the time and the best practice, [please see the guide on GitHub Action here](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule).
