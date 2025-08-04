/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejerciciochatobservables;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;

/**
 *
 * @author Ricardo Alberto
 */
public class Cliente implements Runnable{

    /**
     * @param args the command line arguments
     */
    
    private int puerto;
    private String mensaje;
    
    public Cliente(int puerto,String mensaje){
      this.puerto=puerto;
      this.mensaje=mensaje;
    }
    
    @Override
    public void run() {
        
        final String HOST="127.0.0.1";//Direccion local
        
       
        DataOutputStream out;
        try{
        Socket sc=new Socket(HOST,puerto);
       
        out=new DataOutputStream(sc.getOutputStream());
         out.writeUTF(mensaje);
      
       sc.close();
        
        }catch(Exception ex){
        
        }
        
    }
    
}
