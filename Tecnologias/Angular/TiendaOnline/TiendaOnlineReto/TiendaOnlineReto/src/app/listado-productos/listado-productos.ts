import { Component } from '@angular/core';
import { productoObjeto } from '../producto/productoObjeto';
import { Producto } from '../producto/producto';
import { Formulario } from '../formulario/formulario';

@Component({
  selector: 'app-listado-productos',
  imports: [Producto,Formulario],
  templateUrl: './listado-productos.html',
  styleUrl: './listado-productos.css'
})
export class ListadoProductos {
    productos: productoObjeto[] = [
    new productoObjeto('Pantalón', 130.0),
    new productoObjeto('Camisa', 80.0),
    new productoObjeto('Playera', 50.0),
    ];

    agregarProducto(producto: productoObjeto){
    this.productos.push(producto);
    }
}
