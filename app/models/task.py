from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, default=None)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        if self.completed_at:

            return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": True
            }
        if self.goal_id and not self.completed_at:
            return {
                "id": self.task_id,
                "goal_id": self.goal_id,
                "title": self.title,
                "description": self.description,
                "is_complete": False
            }

        else:
            return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": False
            }


    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(title=task_data["title"],
                    description=task_data["description"])
        return new_task