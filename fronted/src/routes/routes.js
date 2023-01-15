import routesAdmin from "./routes.admin";
import routesCliente from "./routes.cliente";
import { Error404 } from "../Pages";
import { LayoutBasic } from "../layouts";

const routes =[...routesAdmin, ...routesCliente, {
    layout: LayoutBasic,
    component: Error404
}];
export default routes;