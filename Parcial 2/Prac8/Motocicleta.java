public class Motocicleta extends Vehiculo{

    public Motocicleta(String marca, String Modelo, int anio) {
        this.marca = marca;
        this.modelo = Modelo;
        this.anio = anio;
    }

    @Override
    public void encender() {
        super.encender();
        System.out.println("Se ha prendido la motocicleta");
    }

    public void apagar(){
        super.apagar();
        System.out.println("Se ha apagado la motocicleta");
    }

    @Override
    public void describir() {
        super.describir();
        System.out.println("La marca de la motocicleta es: " + marca);
        System.out.println("Modelo de la motocicleta es: " + modelo);
        System.out.println("Anio de la motocicleta es: " + anio);
    }
}