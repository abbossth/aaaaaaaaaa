using System.Collections.Generic;
using RecipeManagementSystem.Models;

namespace RecipeManagementSystem.Services
{
    public interface IRecipeService
    {
        List<Recipe> GetAll();
        Recipe GetById(Guid id);
        void Add(Recipe recipe);
        void Update(Guid id, Recipe recipe);
        void Delete(Guid id);
        List<Recipe> Search(string keyword);
    }
}
