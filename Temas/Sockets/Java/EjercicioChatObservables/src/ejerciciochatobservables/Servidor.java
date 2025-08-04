/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejerciciochatobservables;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
//Clase poder obtener el patron de diseño Observable
import java.util.Observable;

/**
 *
 * @author Ricardo Alberto
 */

//Hereda de la clase observable
public class Servidor extends Observable implements Runnable {

    private int puerto;
    
    public Servidor(int puerto){
    
      this.puerto=puerto;
    }
    
    
    @Override
    public void run() {

        ServerSocket servidor = null;
        Socket sc = null;
        
        DataInputStream in = null;
        

        try {
            servidor = new ServerSocket(puerto);
            while (true) {
                sc = servidor.accept();
                System.out.println("Cliente conectado");
                in = new DataInputStream(sc.getInputStream());
               
                String mensaje = in.readUTF();
                System.out.println(mensaje);

                this.setChanged();//Este notifica a los observadroes que se avesina un cambio
                this.notifyObservers(mensaje);//Manda el elemento a cambiar
                this.clearChanged();//Dice que ya se hizo el cambio
                
                
                sc.close();
                System.out.println("Cliente desconectado");
                //break;
               /* if(mensaje=="salir"){
                 servidor.close();
                 break;
                }*/

            }
            

        } catch (Exception ex) {

        }

    }

}
