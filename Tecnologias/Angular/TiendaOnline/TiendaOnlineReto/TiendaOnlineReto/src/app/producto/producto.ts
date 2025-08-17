import { Component, Input } from '@angular/core';
import { productoObjeto } from './productoObjeto';

@Component({
  selector: 'app-producto',
  imports: [],
  templateUrl: './producto.html',
  styleUrl: './producto.css'
})
export class Producto {
   @Input() producto!: productoObjeto;
}
