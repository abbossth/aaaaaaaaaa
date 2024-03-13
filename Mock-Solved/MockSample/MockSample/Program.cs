using RecipeManagementSystem.Models;
using RecipeManagementSystem.Services;
using System;

namespace RecipeManagementSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            var recipeService = new RecipeService();
            string userInput = "";

            do
            {
                Console.WriteLine("Recipe Management System");
                Console.WriteLine("1. Create Recipe");
                Console.WriteLine("2. Edit Recipe");
                Console.WriteLine("3. Delete Recipe");
                Console.WriteLine("4. Search Recipe");
                Console.WriteLine("5. List All Recipes");
                Console.WriteLine("Q. Quit");
                Console.Write("Select an option: ");

                userInput = Console.ReadLine();

                switch (userInput)
                {
                    case "1":
                        CreateRecipe(recipeService);
                        break;
                    case "2":
                        EditRecipe(recipeService);
                        break;
                    case "3":
                        DeleteRecipe(recipeService);
                        break;
                    case "4":
                        SearchRecipe(recipeService);
                        break;
                    case "5":
                        ListAllRecipes(recipeService);
                        break;
                }

                Console.WriteLine();

            } while (!userInput.Equals("Q", StringComparison.OrdinalIgnoreCase));
        }

        private static void CreateRecipe(IRecipeService recipeService)
        {
            var recipe = new Recipe();

            Console.Write("Enter recipe name: ");
            recipe.Name = Console.ReadLine();

            Console.Write("Enter recipe description: ");
            recipe.Description = Console.ReadLine();

            recipeService.Add(recipe);
            Console.WriteLine("Recipe added successfully!");
        }

        private static void EditRecipe(IRecipeService recipeService)
        {
            Console.Write("Enter recipe ID to edit: ");
            var id = Guid.Parse(Console.ReadLine());

            var existingRecipe = recipeService.GetById(id);
            if (existingRecipe == null)
            {
                Console.WriteLine("Recipe not found!");
                return;
            }

            Console.Write("Enter new name: ");
            existingRecipe.Name = Console.ReadLine();

            Console.Write("Enter new description: ");
            existingRecipe.Description = Console.ReadLine();

            recipeService.Update(id, existingRecipe);
            Console.WriteLine("Recipe updated successfully!");
        }

        private static void DeleteRecipe(IRecipeService recipeService)
        {
            Console.Write("Enter recipe ID to delete: ");
            var id = Guid.Parse(Console.ReadLine());

            recipeService.Delete(id);
            Console.WriteLine("Recipe deleted successfully!");
        }

        private static void SearchRecipe(IRecipeService recipeService)
        {
            Console.Write("Enter keyword to search: ");
            var keyword = Console.ReadLine();

            var results = recipeService.Search(keyword);
            if (results.Count == 0)
            {
                Console.WriteLine("No recipes found!");
            }
            else
            {
                foreach (var recipe in results)
                {
                    Console.WriteLine($"ID: {recipe.Id}, Name: {recipe.Name}, Description: {recipe.Description}");
                }
            }
        }

        private static void ListAllRecipes(IRecipeService recipeService)
        {
            var recipes = recipeService.GetAll();
            if (recipes.Count == 0)
            {
                Console.WriteLine("No recipes available.");
            }
            else
            {
                foreach (var recipe in recipes)
                {
                    Console.WriteLine($"ID: {recipe.Id}, Name: {recipe.Name}, Description: {recipe.Description}");
                }
            }
        }

        //HINTS for Mock
        /*
         * See mocking seminar.
         var transactionLoggerMock = new Mock<TransactionLogger>();
            BankAccount account = new BankAccount(transactionLoggerMock.Object);

            // Act
            account.Deposit(500);

            // Assert
            transactionLoggerMock.Verify(
                logger => logger.LogTransaction("Deposit", 500),
                Times.Once); 
         
         */
    }
}
