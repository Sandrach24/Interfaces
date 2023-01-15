 import { ClienteLayout } from "../layouts";
 import { Home, Emprendimiento } from "../Pages/Cliente";
 

 const routesCliente = [
    {
        path: "/",
        layout: ClienteLayout,
        component: Home,
    },
    {
        path: "/emprendimiento",
        layout: ClienteLayout,
        component: Emprendimiento,
    },
];

export default routesCliente;