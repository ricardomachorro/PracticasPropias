
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ricardo Alberto
 */



/*

Clase ejemplo inicio de conexion con sockets de flujo


Son un servicio orientado a la conexión, donde los datos se
transfieren sin encuadrarlos en registros o bloques

Si se rompe la conexión entre los procesos , estos 
seran informados de tal suceso para que tomen las medidas
oportunas

*/
public class Cliente {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        final String HOST="127.0.0.1";//Direccion local
        final int PUERTO=5000;
        DataInputStream in;
        DataOutputStream out;
        
        
       try{ 
        Socket sc=new Socket(HOST,PUERTO);
       in=new DataInputStream(sc.getInputStream());
       out=new DataOutputStream(sc.getOutputStream());
       out.writeUTF("!Hola mundo desde el cliente");
       String mensaje=in.readUTF();
       System.out.println(mensaje);
       sc.close();
       
       }catch(Exception ex){
       System.out.println(ex.toString());
       }
    }
    
}
