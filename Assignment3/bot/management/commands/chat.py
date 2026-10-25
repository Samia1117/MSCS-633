"""
Terminal chat client.

Run with:  python manage.py chat

Builds a ChatterBot instance, trains it on the conversations in
bot/training_data.py, and then loops reading from the user and printing
the bot's reply until the user types quit/exit/bye or presses Ctrl+C.
"""

from django.conf import settings
from django.core.management.base import BaseCommand

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from bot.training_data import CONVERSATIONS

# Words that end the chat session
EXIT_WORDS = {"quit", "exit", "bye"}


def build_bot(retrain: bool = False) -> ChatBot:
    """Create the ChatBot and train it if it has not been trained yet."""
    bot = ChatBot(
        "Terminal Bot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        # Keep the learned data in a sqlite file next to manage.py
        database_uri=f"sqlite:///{settings.BASE_DIR / 'chatbot_db.sqlite3'}",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                # Used when no stored statement matches well enough
                "default_response": "Sorry, I do not understand. Can you say that another way?",
                "maximum_similarity_threshold": 0.90,
            }
        ],
    )

    # Only train on first run (or when --retrain is passed) so startup is quick
    if retrain:
        bot.storage.drop()
    if retrain or bot.storage.count() == 0:
        trainer = ListTrainer(bot)
        for conversation in CONVERSATIONS:
            trainer.train(conversation)
    return bot


class Command(BaseCommand):
    help = "Chat with a ChatterBot-powered bot in the terminal."

    def add_arguments(self, parser):
        parser.add_argument(
            "--retrain",
            action="store_true",
            help="Wipe the stored data and train the bot again from scratch.",
        )

    def handle(self, *args, **options):
        bot = build_bot(retrain=options["retrain"])
        self.stdout.write("Chat started. Type 'quit' to leave.\n")

        while True:
            try:
                user_text = input("user: ").strip()
            except (KeyboardInterrupt, EOFError):
                # Ctrl+C / Ctrl+D: leave cleanly
                self.stdout.write("\nbot: Goodbye!")
                break

            if not user_text:
                continue  # ignore blank lines

            if user_text.lower() in EXIT_WORDS:
                self.stdout.write("bot: Goodbye! Have a nice day.")
                break

            reply = bot.get_response(user_text)
            self.stdout.write(f"bot: {reply}")
