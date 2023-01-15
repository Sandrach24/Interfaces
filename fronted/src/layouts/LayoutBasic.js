import React  from "react";

export function LayoutBasic(props){
    const {children} = props;
    return (
        <div>
            <h1>Layout basica</h1>
            {children}
        </div>
    );
}