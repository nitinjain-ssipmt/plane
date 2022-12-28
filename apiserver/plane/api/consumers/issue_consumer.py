from channels.generic.websocket import SyncConsumer
import json
from plane.db.models import IssueActivity, Project, User, Issue, State, Label


class IssueConsumer(SyncConsumer):

    # Track Chnages in name
    def track_name(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("name") != requested_data.get("name"):
            issue_activities.append(
                IssueActivity(
                    issue_id=issue_id,
                    actor=actor,
                    verb="updated",
                    old_value=current_instance.get("name"),
                    new_value=requested_data.get("name"),
                    field="name",
                    project=project,
                    workspace=project.workspace,
                    comment=f"{actor.email} updated the start date to {requested_data.get('name')}",
                )
            )

    # Track changes in parent issue
    def track_parent(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("parent") != requested_data.get("parent"):

            if requested_data.get("parent") == None:
                old_parent = Issue.objects.get(pk=current_instance.get("parent"))
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=f"{project.identifier}-{old_parent.sequence_id}",
                        new_value=None,
                        field="parent",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the parent issue to None",
                    )
                )
            else:
                new_parent = Issue.objects.get(pk=requested_data.get("parent"))
                old_parent = Issue.objects.filter(
                    pk=current_instance.get("parent")
                ).first()
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=f"{project.identifier}-{old_parent.sequence_id}"
                        if old_parent is not None
                        else None,
                        new_value=f"{project.identifier}-{new_parent.sequence_id}",
                        field="parent",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the parent issue to {new_parent.name}",
                    )
                )

    # Track changes in priority
    def track_priority(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("priority") != requested_data.get("priority"):
            if requested_data.get("priority") == None:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("parent"),
                        new_value=requested_data.get("parent"),
                        field="priority",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the priority to None",
                    )
                )
            else:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("priority"),
                        new_value=requested_data.get("priority"),
                        field="priority",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the priority to {requested_data.get('priority')}",
                    )
                )

    # Track chnages in state of the issue
    def track_state(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("state") != requested_data.get("state"):

            new_state = State.objects.get(pk=requested_data.get("state", None))
            old_state = State.objects.get(pk=current_instance.get("state", None))

            issue_activities.append(
                IssueActivity(
                    issue_id=issue_id,
                    actor=actor,
                    verb="updated",
                    old_value=old_state.name,
                    new_value=new_state.name,
                    field="state",
                    project=project,
                    workspace=project.workspace,
                    comment=f"{actor.email} updated the state to {new_state.name}",
                )
            )

    # Track issue description
    def track_description(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("description") != requested_data.get("description"):

            issue_activities.append(
                IssueActivity(
                    issue_id=issue_id,
                    actor=actor,
                    verb="updated",
                    old_value=current_instance.get("description"),
                    new_value=requested_data.get("description"),
                    field="description",
                    project=project,
                    workspace=project.workspace,
                    comment=f"{actor.email} updated the description to {requested_data.get('description')}",
                )
            )

    # Track changes in issue target date
    def track_target_date(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("target_date") != requested_data.get("target_date"):
            if requested_data.get("target_date") == None:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("target_date"),
                        new_value=requested_data.get("target_date"),
                        field="target_date",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the target date to None",
                    )
                )
            else:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("target_date"),
                        new_value=requested_data.get("target_date"),
                        field="target_date",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the target date to {requested_data.get('target_date')}",
                    )
                )

    # Track changes in issue start date
    def track_start_date(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        if current_instance.get("start_date") != requested_data.get("start_date"):
            if requested_data.get("start_date") == None:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("start_date"),
                        new_value=requested_data.get("start_date"),
                        field="start_date",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the start date to None",
                    )
                )
            else:
                issue_activities.append(
                    IssueActivity(
                        issue_id=issue_id,
                        actor=actor,
                        verb="updated",
                        old_value=current_instance.get("start_date"),
                        new_value=requested_data.get("start_date"),
                        field="start_date",
                        project=project,
                        workspace=project.workspace,
                        comment=f"{actor.email} updated the start date to {requested_data.get('start_date')}",
                    )
                )

    # Track changes in issue labels
    def track_labels(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):
        # Label Addition
        if len(requested_data.get("labels_list")) > len(current_instance.get("labels")):

            for label in requested_data.get("labels_list"):
                if label not in current_instance.get("labels"):
                    label = Label.objects.get(pk=label)
                    issue_activities.append(
                        IssueActivity(
                            issue_id=issue_id,
                            actor=actor,
                            verb="updated",
                            old_value="",
                            new_value=label.name,
                            field="labels",
                            project=project,
                            workspace=project.workspace,
                            comment=f"{actor.email} added label {label.name}",
                        )
                    )

        # Label Removal
        if len(requested_data.get("labels_list")) < len(current_instance.get("labels")):

            for label in current_instance.get("labels"):
                if label not in requested_data.get("labels_list"):
                    label = Label.objects.get(pk=label)
                    issue_activities.append(
                        IssueActivity(
                            issue_id=issue_id,
                            actor=actor,
                            verb="updated",
                            old_value=label.name,
                            new_value="",
                            field="labels",
                            project=project,
                            workspace=project.workspace,
                            comment=f"{actor.email} removed label {label.name}",
                        )
                    )

    # Track changes in issue assignees
    def track_assignees(
        self,
        requested_data,
        current_instance,
        issue_id,
        project,
        actor,
        issue_activities,
    ):

        # Assignee Addition
        if len(requested_data.get("assignees_list")) > len(
            current_instance.get("assignees")
        ):

            for assignee in requested_data.get("assignees_list"):
                if assignee not in current_instance.get("assignees"):
                    assignee = User.objects.get(pk=assignee)
                    issue_activities.append(
                        IssueActivity(
                            issue_id=issue_id,
                            actor=actor,
                            verb="updated",
                            old_value="",
                            new_value=assignee.email,
                            field="assignees",
                            project=project,
                            workspace=project.workspace,
                            comment=f"{actor.email} added assignee {assignee.email}",
                        )
                    )

        # Assignee Removal
        if len(requested_data.get("assignees_list")) < len(
            current_instance.get("assignees")
        ):

            for assignee in current_instance.get("assignees"):
                if assignee not in requested_data.get("assignees_list"):
                    assignee = User.objects.get(pk=assignee)
                    issue_activities.append(
                        IssueActivity(
                            issue_id=issue_id,
                            actor=actor,
                            verb="updated",
                            old_value=assignee.email,
                            new_value="",
                            field="assignee",
                            project=project,
                            workspace=project.workspace,
                            comment=f"{actor.email} removed assignee {assignee.email}",
                        )
                    )

    # Receive message from room group
    def issue_activity(self, event):

        issue_activities = []
        # Remove event type:
        event.pop("type")

        requested_data = json.loads(event.get("requested_data"))
        current_instance = json.loads(event.get("current_instance"))
        issue_id = event.get("issue_id")
        actor_id = event.get("actor_id")
        project_id = event.get("project_id")

        actor = User.objects.get(pk=actor_id)

        project = Project.objects.get(pk=project_id)

        ISSUE_ACTIVITY_MAPPER = {
            "name": self.track_name,
            "parent": self.track_parent,
            "priority": self.track_priority,
            "state": self.track_state,
            "description": self.track_description,
            "target_date": self.track_target_date,
            "start_date": self.track_start_date,
            "labels_list": self.track_labels,
            "assignees_list": self.track_assignees,
        }

        for key in requested_data:
            func = ISSUE_ACTIVITY_MAPPER.get(key, None)
            if func is not None:
                func(
                    requested_data,
                    current_instance,
                    issue_id,
                    project,
                    actor,
                    issue_activities,
                )

        # TODO: Add blocking and blocker issue tracking once cleared from frontend
        IssueActivity.objects.bulk_create(issue_activities)
