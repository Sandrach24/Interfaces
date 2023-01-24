import React from 'react'

export  function Header() {
  return (
    <div>
        <header className='header'>
            <div className='header_box'>
                <span className='header_primary'>UIDE -Loja</span>
            </div>

            <div className='text_box'> 
                <h1 className='primario'>
                    <span className='primario_main'> Bienvenidos al sitio de emprendimientos</span>
                    <span className='primario_sub'>San Pedro de Vilcabamba </span>
                
                </h1>
                <a href='/' class='btn btn-white btn-animated'>
                    Realiza turismo ecologico con la del emprendimiento
                </a>

            </div>

        </header>
    </div>
  )
}


