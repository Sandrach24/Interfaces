import { AdminLayout } from "../layouts";
import { HomeAdmin } from "../Pages/Admin";

const routesAdmin = [
    {
        path: "/admin",
        layout: AdminLayout,
        component: HomeAdmin,
        exac:true,
    }
]

export default routesAdmin;
