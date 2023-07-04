"""
[3] select employee.name, employee.address
    from employee, company, affiliation
    where affiliation.employee_id = employee.employee_id and
        affiliation.company_id = company.company_id and
        company.name = '천국테크'
    order by employee.name;

[4] select employee.name, company.name, company.address, employee.address
    from employee, company, affiliation
    where affiliation.employee_id = employee.employee_id and
        affiliation.company_id = company.company_id and
        company.address != employee.address
    order by employee.name;

[5] select company.name, count(employee.employee_id) as count, avg(affiliation.pay) as average
    from employee, company, affiliation
    where affiliation.employee_id = employee.employee_id and
        affiliation.company_id = company.company_id
    group by company.name
    order by company.name

[6]

"""