import { AdminLayout } from "../layouts";
import { LoginAdmin } from "../Pages";

const routesAdmin = [
    {
        path: "/admin",
        layout: AdminLayout,
        component: LoginAdmin,
    }
]

export default routesAdmin;
