import React from 'react'
import {Menu, Input} from 'semantic-ui-react'
import   './Footer.scss';

export  function Footer() {
  return (
    <div>
        <Menu>
            <Menu.Item disabled>
                (c) Desarrollo Realizado por la asignatura de Interfaces y Multimedia
            </Menu.Item>
            <Menu.Item position='right'>
                <Input disabled label='Autor> Interfaces y Multimedia'></Input>
            </Menu.Item>
            <Menu.Item>
                <Input disabled label='Anio 2023'> </Input>
            </Menu.Item>
        </Menu>

        <footer className= 'container'>
            <h1 className='container__letra' >Footer UIDE </h1>
            <p className='container__parrafo'>
                (c) Proyecto Desarrollo en IM <br/>
                <a href='/'>Politicas</a>

            </p> 
           
        </footer>

    </div>
  )
}
