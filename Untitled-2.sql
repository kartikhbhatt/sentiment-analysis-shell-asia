select * from invoice_validation_rules

-- To update the name and email for each country in UAM_SuperUser, use an UPDATE statement.
-- Example: Update name and email for a specific country (e.g., 'India')

UPDATE [dbo].[UAM_SuperUser]
SET [name] = 'Prateek Sharma', [email] = 'Prateek.Sharma@shell.com'
WHERE [country] = 'India';
UPDATE [dbo].[UAM_SuperUser]
SET [name] = 'Big Brain Baljet', [email] = 'Anubhav.Kini@shell.com'
WHERE [country] = 'Singapore';
UPDATE [dbo].[UAM_SuperUser]
SET [name] = 'Aniket k', [email] = 'Aniket.A.Kulkarni@shell.com'
WHERE [country] = 'Oman';

-- Repeat or adjust the WHERE clause for other countries as needed.
-- To update multiple countries at once with different values, use CASE:

select * from [dbo].[UAM_SuperUser];
select * from [dbo].[UAM_master] order by AddedAt desc;

DELETE FROM [dbo].[UAM_master]

select * from [dbo].[vw_approval_log_details]

UPDATE [dbo].[UAM_SuperUser]
set [email] = 'adarsh.nag@shell.com'
WHERE [name] = 'Adarsh Nag';



select * from [dbo].[UAM_SuperUser];

select * from [dbo].[UAM_master] order by AddedAt desc;

select * from [dbo].[Invoice_master] order by created_date desc;

select * from [dbo].[dit_invoice_log] order by invoice_id, [Timestamp] desc;

delete from [dbo].[UAM_master];

select count(*) from [dbo].[UAM_master] where BusinessDecision = 1;


select * from [dbo].[UAM_master] where BusinessDecision is not NULL order by BusinessDecision;


alter table [dbo].[UAM_master]
add [MessageId] nvarchar(100);

select * from [dbo].[invoice_master] where invoice_id = 'DAY110010811';

select * from vendors_master where po= '4546032308';
-- 11277025.0000



delete from [dbo].[dit_approval_log]; delete from [dbo].[dit_approval_log1]; delete from [dbo].[dit_invoice_log]; delete from [dbo].[Invoice_master]; delete from [dbo].[invoice_validation_audit]; delete from [dbo].[invoice_validation_log];
