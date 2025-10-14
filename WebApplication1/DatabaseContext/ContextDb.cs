using Microsoft.EntityFrameworkCore;
using System;
using WebApplication1.Models;


namespace WebApplication1.DatabaseContext
{
    public class ContextDb : DbContext
    {
        public ContextDb(DbContextOptions<ContextDb> options)
         : base(options) { }

       public DbSet<Order> Orders { get; set; }
       
    }
}
