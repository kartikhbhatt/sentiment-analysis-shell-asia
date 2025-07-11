select * from UAM_master ;
select count(*) from UAM_master;
select * from UAM_master where Country ='Indonesia';
select count(*) from UAM_dump;
select distinct Country from UAM_master;
select * from UAM_SuperUser;
select * from [dbo].[UAM_dump];

TRUNCATE TABLE UAM_dump;
TRUNCATE TABLE UAM_master;
DELETE FROM uam_master WHERE country = 'Indonesia';

-- Update the email address for a specific approver in the vendors_master table
UPDATE vendors_master
SET Approver_for_SES_GR = 'Aritra.Kundu@shell.com'
WHERE Approver_for_SES_GR = 'Aritra Kundu';

select * from vendors_master where Approver_for_SES_GR = 'Aritra.Kundu@shell.com';
select * from vendors_master where Approver_for_SES_GR = 'Aritra Kundu';

select * from dit_approval_log;

select * from uam_master;
select * from UAM_dump;



ALTER TABLE dit_approval_log
ALTER COLUMN [TimeStamp] NVARCHAR(4000);

select * from dit_approval_log;
-- drop table [dbo].[dit_approval_log];

ALTER TABLE [dbo].[dit_approval_log]
ADD CONSTRAINT [PK_dit_approval_log_Id] PRIMARY KEY NONCLUSTERED ([Id], [TimeStamp]) NOT ENFORCED;
GO

ALTER TABLE [dbo].[dit_approval_log]
ALTER COLUMN [TimeStamp] NVARCHAR(255) NOT NULL;
GO
ALTER TABLE [dbo].[dit_approval_log]
ALTER COLUMN [Id] BIGINT NOT NULL;
GO

-- to make the primary key non-clustered and not enforced 
ALTER TABLE dit_approval_log
ADD CONSTRAINT PK_ PRIMARY KEY NONCLUSTERED (Email, AddedAt) NOT ENFORCED;

ALTER TABLE UAM_master
ALTER COLUMN [AddedAt] DATETIME NOT NULL;
GO
ALTER TABLE UAM_master
ALTER COLUMN [Email] NVARCHAR(4000) NOT NULL;
GO
