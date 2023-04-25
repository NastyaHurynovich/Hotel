from user_role.widgets import PermissionsSelectMultiply as UserRolePermissionsSelectMultiply


class PermissionsSelectMultiply(UserRolePermissionsSelectMultiply):
    groups_permissions = {
        "Номера": ["rooms.rooms"],
        "Пользователи и роли": ["user_role.role", "core.user"],
        "Заказы": ["orders.orders"]
    }
