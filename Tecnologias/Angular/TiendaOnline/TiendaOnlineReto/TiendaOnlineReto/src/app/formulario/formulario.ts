import { Component, ElementRef, EventEmitter, Output, ViewChild} from '@angular/core';
import { productoObjeto } from '../producto/productoObjeto';

@Component({
  selector: 'app-formulario',
  imports: [],
  templateUrl: './formulario.html',
  styleUrl: './formulario.css'
})
export class Formulario {

  @ViewChild('descripcionInput') descripcionInput!: ElementRef;
  @ViewChild('precioInput') precioInput!: ElementRef;
  @Output() nuevoProducto = new EventEmitter<productoObjeto>();

  agregarProducto(evento: Event){
      evento.preventDefault();
      //Validar que sean valores correcto
      if(this.descripcionInput.nativeElement.value.trim() === ''
       || this.precioInput == null || this.precioInput.nativeElement.value <=0){
        console.log('Debe ingresar una descripción y un precio válidos');
        return;
      }
      const producto = new productoObjeto(this.descripcionInput.nativeElement.value,
      this.precioInput.nativeElement.value);
      //Emitir el evento de nuevo producto
      this.nuevoProducto.emit(producto);
      // Limpiamos los campos del formulario
      this.descripcionInput.nativeElement.value = '';
      this.precioInput.nativeElement.value = null;
    }



}
