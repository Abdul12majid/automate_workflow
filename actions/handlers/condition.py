from actions.utils.variables import insert


class ConditionHandler:

    @staticmethod
    def run(config, context):

        left = insert(
            config["left"],
            context
        )

        right = insert(
            config["right"],
            context
        )

        operator = config["operator"]

        if operator == "equals":
            return left == right

        if operator == "not_equals":
            return left != right

        if operator == "contains":
            return str(right) in str(left)

        if operator == "greater_than":
            return left > right

        if operator == "less_than":
            return left < right

        return False