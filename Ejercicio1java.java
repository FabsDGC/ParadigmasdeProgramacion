import java.util.Scanner;


//PARADIGMAS DE PROGRAMACIÓN
//MADE BY FABS 3BV2
public class FigurasGeometricas {

    // Función del círculo
    public static void circulo() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce el radio del círculo en metros: ");
        double radio = scanner.nextDouble();

        System.out.println("1. Calcular Área");
        System.out.println("2. Calcular Perímetro");
        System.out.println("3. Calcular Ambos");
        System.out.print("Elige una opción: ");
        String opcion = scanner.next();

        switch (opcion) {
            case "1":
                double area_m = Math.PI * Math.pow(radio, 2);
                System.out.printf("Área del círculo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                break;
            case "2":
                double perimetro_m = 2 * Math.PI * radio;
                System.out.printf("Perímetro del círculo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            case "3":
                area_m = Math.PI * Math.pow(radio, 2);
                perimetro_m = 2 * Math.PI * radio;
                System.out.printf("Área del círculo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                System.out.printf("Perímetro del círculo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    // Función del cuadrado
    public static void cuadrado() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce el lado del cuadrado en metros: ");
        double lado = scanner.nextDouble();

        System.out.println("1. Calcular Área");
        System.out.println("2. Calcular Perímetro");
        System.out.println("3. Calcular Ambos");
        System.out.print("Elige una opción: ");
        String opcion = scanner.next();

        switch (opcion) {
            case "1":
                double area_m = Math.pow(lado, 2);
                System.out.printf("Área del cuadrado: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                break;
            case "2":
                double perimetro_m = 4 * lado;
                System.out.printf("Perímetro del cuadrado: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            case "3":
                area_m = Math.pow(lado, 2);
                perimetro_m = 4 * lado;
                System.out.printf("Área del cuadrado: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                System.out.printf("Perímetro del cuadrado: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    // Función del rectángulo
    public static void rectangulo() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce el largo del rectángulo en metros: ");
        double largo = scanner.nextDouble();
        System.out.print("Introduce el ancho del rectángulo en metros: ");
        double ancho = scanner.nextDouble();

        System.out.println("1. Calcular Área");
        System.out.println("2. Calcular Perímetro");
        System.out.println("3. Calcular Ambos");
        System.out.print("Elige una opción: ");
        String opcion = scanner.next();

        switch (opcion) {
            case "1":
                double area_m = largo * ancho;
                System.out.printf("Área del rectángulo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                break;
            case "2":
                double perimetro_m = 2 * (largo + ancho);
                System.out.printf("Perímetro del rectángulo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            case "3":
                area_m = largo * ancho;
                perimetro_m = 2 * (largo + ancho);
                System.out.printf("Área del rectángulo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                System.out.printf("Perímetro del rectángulo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    // Función del triángulo
    public static void triangulo() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce la base del triángulo en metros: ");
        double base = scanner.nextDouble();
        System.out.print("Introduce la altura del triángulo en metros: ");
        double altura = scanner.nextDouble();
        System.out.print("Introduce el lado 1 del triángulo en metros: ");
        double lado1 = scanner.nextDouble();
        System.out.print("Introduce el lado 2 del triángulo en metros: ");
        double lado2 = scanner.nextDouble();

        System.out.println("1. Calcular Área");
        System.out.println("2. Calcular Perímetro");
        System.out.println("3. Calcular Ambos");
        System.out.print("Elige una opción: ");
        String opcion = scanner.next();

        switch (opcion) {
            case "1":
                double area_m = (base * altura) / 2;
                System.out.printf("Área del triángulo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                break;
            case "2":
                double perimetro_m = base + lado1 + lado2;
                System.out.printf("Perímetro del triángulo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            case "3":
                area_m = (base * altura) / 2;
                perimetro_m = base + lado1 + lado2;
                System.out.printf("Área del triángulo: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                System.out.printf("Perímetro del triángulo: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    // Función del trapecio
    public static void trapecio() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce la base mayor del trapecio en metros: ");
        double baseMayor = scanner.nextDouble();
        System.out.print("Introduce la base menor del trapecio en metros: ");
        double baseMenor = scanner.nextDouble();
        System.out.print("Introduce la altura del trapecio en metros: ");
        double altura = scanner.nextDouble();
        System.out.print("Introduce el lado 1 del trapecio en metros: ");
        double lado1 = scanner.nextDouble();
        System.out.print("Introduce el lado 2 del trapecio en metros: ");
        double lado2 = scanner.nextDouble();

        System.out.println("1. Calcular Área");
        System.out.println("2. Calcular Perímetro");
        System.out.println("3. Calcular Ambos");
        System.out.print("Elige una opción: ");
        String opcion = scanner.next();

        switch (opcion) {
            case "1":
                double area_m = ((baseMayor + baseMenor) * altura) / 2;
                System.out.printf("Área del trapecio: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                break;
            case "2":
                double perimetro_m = baseMayor + baseMenor + lado1 + lado2;
                System.out.printf("Perímetro del trapecio: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            case "3":
                area_m = ((baseMayor + baseMenor) * altura) / 2;
                perimetro_m = baseMayor + baseMenor + lado1 + lado2;
                System.out.printf("Área del trapecio: %.2f m² (%.2f cm²)%n", area_m, area_m * 10000);
                System.out.printf("Perímetro del trapecio: %.2f m (%.2f cm)%n", perimetro_m, perimetro_m * 100);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    // Función del menú
    public static void menu() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Menú de cálculo de área y perímetro");
            System.out.println("1. Círculo");
            System.out.println("2. Cuadrado");
            System.out.println("3. Rectángulo");
            System.out.println("4. Triángulo");
            System.out.println("5. Trapecio");
            System.out.println("6. Salir");

            System.out.print("Elige una opción: ");
            String opcion = scanner.next();

            switch (opcion) {
                case "1":
                    circulo();
                    break;
                case "2":
                    cuadrado();
                    break;
                case "3":
                    rectangulo();
                    break;
                case "4":
                    triangulo();
                    break;
                case "5":
                    trapecio();
                    break;
                case "6":
                    System.out.println("Saliendo del programa...");
                    return;
                default:
                    System.out.println("Opción no válida. Intenta de nuevo.\n");
            }
        }
    }

    // Método principal para ejecutar el menú
    public static void main(String[] args) {
        menu();
    }
}
