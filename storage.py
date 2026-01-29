import json
from datetime import datetime
from pathlib import Path


class ResultsStorage:
    def __init__(self):
        # Store results in user's home directory
        self.data_dir = Path.home() / ".hypertype"
        self.results_file = self.data_dir / "results.json"

        # Create directory if it doesn't exist
        self.data_dir.mkdir(exist_ok=True)

        # Create file if it doesn't exist
        if not self.results_file.exists():
            self.results_file.write_text("[]")

    def save_result(self, result: dict):
        """Save a test result"""
        # Add timestamp
        result["timestamp"] = datetime.now().isoformat()

        # Load existing results
        results = self.load_results()

        # Add new result
        results.append(result)

        # Save back to file
        with open(self.results_file, "w") as f:
            json.dump(results, f, indent=2)

        return True

    def load_results(self):
        """Load all past results"""
        try:
            with open(self.results_file, "r") as f:
                return json.load(f)
        except:
            return []

    def get_stats(self):
        """Get statistics from all results"""
        results = self.load_results()

        if not results:
            return None

        total_tests = len(results)
        avg_wpm = sum(r["wpm"] for r in results) / total_tests
        avg_accuracy = sum(r["accuracy"] for r in results) / total_tests
        best_wpm = max(r["wpm"] for r in results)
        best_accuracy = max(r["accuracy"] for r in results)

        return {
            "total_tests": total_tests,
            "avg_wpm": round(avg_wpm, 2),
            "avg_accuracy": round(avg_accuracy, 2),
            "best_wpm": round(best_wpm, 2),
            "best_accuracy": round(best_accuracy, 2),
        }

    def get_recent_results(self, count: int = 10):
        """Get the most recent results"""
        results = self.load_results()
        return results[-count:] if results else []
