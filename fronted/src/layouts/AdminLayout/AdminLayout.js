import React from 'react';
import './AdminLayout.scss';

export function AdminLayout( props ){
    const { children } = props;

 return (
     <div>
        <h1> Pagina establecida para el administrador del sistema </h1>
        {children}
     </div>
    )
}