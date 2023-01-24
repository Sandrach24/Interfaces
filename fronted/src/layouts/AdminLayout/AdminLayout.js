import React from 'react';
import { LoginAdmin } from '../../Pages/Admin/LoginAdmin';
import './AdminLayout.scss';

export function AdminLayout( props ){
    const { children } = props;
    const auth=null

    if (!auth) return <LoginAdmin/>

 return (
     <div>
       <p>Pantalla de administrador</p>
        {children}
     </div>
    )
}