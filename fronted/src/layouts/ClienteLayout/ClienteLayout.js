import React from "react";   
import './ClienteLayout.scss';

 export function ClienteLayout(props) {
    const {children} = props;
    return (
        <div>
            <h1>Cliente desarrollada para el cliente</h1>
            {children}
        </div>
    );

}