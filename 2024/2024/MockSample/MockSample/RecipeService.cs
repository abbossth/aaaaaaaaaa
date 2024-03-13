using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using RecipeManagementSystem.Models;
using System.Linq;
using System.Xml;
using Formatting = Newtonsoft.Json.Formatting;

namespace RecipeManagementSystem.Services
{
    public class ActionLogger
    {
        public virtual void LogActions(string Action, string Data)
        {
            // Simulate logging transaction (actual logging implementation can vary)
            Console.WriteLine($"Action logged: {Action} and {Data}" );
        }
    }

    public class RecipeService : IRecipeService
    {
        private readonly string _filePath = "Data/recipes.json";
        private List<Recipe> _recipes;
        private readonly ActionLogger _transactionLogger;

        public RecipeService()
        {
            var jsonData = File.ReadAllText(_filePath);
            _recipes = JsonConvert.DeserializeObject<List<Recipe>>(jsonData, new JsonSerializerSettings
            {
                NullValueHandling = NullValueHandling.Ignore
            });

        }
        public RecipeService(ActionLogger transactionLogger)
        {
            _transactionLogger = transactionLogger ?? throw new ArgumentNullException(nameof(transactionLogger));

            var jsonData = File.ReadAllText(_filePath);
            _recipes = JsonConvert.DeserializeObject<List<Recipe>>(jsonData, new JsonSerializerSettings
            {
                NullValueHandling = NullValueHandling.Ignore
            });

        }

        public List<Recipe> GetAll() => _recipes;

        public Recipe GetById(Guid id) => _recipes.FirstOrDefault(r => r.Id == id);

        public void Add(Recipe recipe)
        {
            _recipes.Add(recipe);
            SaveChanges();

            if(_transactionLogger!=null)
           _transactionLogger.LogActions("Add", recipe.Name);
        }

        public void Update(Guid id, Recipe updatedRecipe)
        {
            var recipe = _recipes.FirstOrDefault(r => r.Id == id);
            if (recipe == null) return;
            recipe.Name = updatedRecipe.Name;
            recipe.Description = updatedRecipe.Description;
            // Update other fields as necessary
            SaveChanges();

            if (_transactionLogger != null)
                _transactionLogger.LogActions("Update", recipe.Name);
        }

        public void Delete(Guid id)
        {
            var recipe = _recipes.FirstOrDefault(r => r.Id == id);
            if (recipe != null)
            {
                _recipes.Remove(recipe);
                SaveChanges();

                if (_transactionLogger != null)
                    _transactionLogger.LogActions("Delete", recipe.Name);
            }
        }

        public List<Recipe> Search(string keyword) =>
            _recipes.Where(r => r.Name.Contains(keyword, StringComparison.OrdinalIgnoreCase) || r.Description.Contains(keyword, StringComparison.OrdinalIgnoreCase)).ToList();

        private void SaveChanges()
        {
            var jsonData = JsonConvert.SerializeObject(_recipes, Formatting.Indented);
            File.WriteAllText(_filePath, jsonData);
        }
    }
}
