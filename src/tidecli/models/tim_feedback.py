"""Provide feedback to console/IDE from TIM."""

from pydantic import BaseModel


class WebData(BaseModel):
    """Contains data from the web response."""

    console: str | None = None
    error: str
    language: str | None = None
    pwd: str | None = None
    runtime: str | None = None


class TimFeedback(BaseModel):
    """Model for feedback response after submitting a task."""

    savedNew: int | None
    valid: bool
    web: WebData | None

    def console_output(self):
        """Return the console output of the task."""
        if self.web.error != "":
            return self.web.error

        if self.savedNew:
            saved_new = "Saved new answer successfully."
        else:
            saved_new = "New answer was not saved. Same file was already submitted."

        return [saved_new, "\nFeedback from TIM:", self.web.console]
